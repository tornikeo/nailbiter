
const MODEL_PATH = '/static/js_models/model.json'
const IMAGE_SIZE = 64;

let webcam;
let model;
let videoElement;
let recordButton;
let predictionElement;

const predictNailbiting = async () => {
  console.log('loading model');
  model = await tf.loadLayersModel(MODEL_PATH)
  model.predict(tf.zeros([1,IMAGE_SIZE,IMAGE_SIZE,3])).dispose();
  console.log('')
  predict(videoElement)
};

const predict = async (imgElement) => {
  console.log('Predicting');
  let img = tf.browser.fromPixels(imgElement)
    .expandDims(0)
    .toInt();
  img = tf.image.resizeBilinear(img, [IMAGE_SIZE, IMAGE_SIZE])
  let canvas = document.querySelector('#canvasElement')

  const prediction = tf.tidy(() => {
    return model.predict(img)
  })
  prediction.data()
    .then((data) => console.log("done!", data))
    .catch(console.log)
}

/**
 * Captures a frame from the webcam and normalizes it between -1 and 1.
 * Returns a batched image (1-element batch) of shape [1, w, h, c].
 */
async function getImage() {
  const img = await webcam.capture();
  const processedImg =
      tf.tidy(() => img.expandDims(0).toFloat().div(127).sub(1));
  img.dispose();
  return processedImg;
}

let intervalId ;
const startLoop = (fn, interval) => {
  intervalId = window.setInterval(fn, interval)
}

const stopLoop = () => {
  clearInterval(intervalId)
}

const getPrediction = async (frame) => {
  return await model.predict(frame).data()
}

const displayPrediction = (prediction, element) => {
  // console.log(element)
  if (prediction[1] > .75) {
    element.textContent = `You are <b> biting </b> nails. I am ${(prediction[1]*100).toFixed(2)}% sure.`
  } else if (prediction[1] > .25) {
    element.textContent = `I'm not sure. I think about ${(prediction[1]*100).toFixed(2)}% that you are biting nails.`
  } else {
    element.textContent = `You are <b> not biting </b> nails. I am ${(prediction[2]*100).toFixed(2)}% sure.`
  }
}

const init = async () => {
  recordButton = document.querySelector("#recordButton");
  videoElement = document.querySelector("#videoElement");
  predictionElement = document.querySelector('#predictionElement')

  recordButton.hidden = true;

  if (navigator.mediaDevices.getUserMedia) {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then( (stream) => {
        videoElement.srcObject = stream;
      })
      .catch(console.log);
  }
  webcam = await tf.data.webcam(videoElement, 
    {resizeWidth:IMAGE_SIZE,
    resizeHeight:IMAGE_SIZE}
  );
  
  model = await tf.loadLayersModel(MODEL_PATH);
  
  //warmup
  let frame = await getImage();
  getPrediction(frame);
  
  recordButton.addEventListener(
    'click',
    ({target}) => {
      if (target.textContent === 'Stop record') {
        target.textContent = 'Record'
        stopLoop()
      } else {
        target.textContent = 'Stop record';
        startLoop(async () => {
          let frame = await getImage();
          let prediction = await getPrediction(frame);
          displayPrediction(prediction, predictionElement)
        }, 300)
      }
    }
  )
  
  recordButton.hidden = false;
  
};

init()






