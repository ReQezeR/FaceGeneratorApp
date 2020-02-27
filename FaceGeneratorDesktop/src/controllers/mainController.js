var remote = require('electron').remote; 
var dialog = remote.dialog;
const BrowserWindow = remote.BrowserWindow;
var fs = require('fs');

/* Global variaables */
var canvas = new CAFECanvas('mainCanvas');

/* CONST Values */
const colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000'];

/* DOM Elements */
const appMinimizeButton = document.querySelector('#appMinimizeButton'),
    appCloseButton = document.querySelector('#appCloseButton');
    
const loadImageButton = document.querySelector('#loadImageButton'),
    uploadItemButton = document.querySelector('#uploadItemButton'),
    saveLocallyButton = document.querySelector('#saveLocallyButton');

const previousVectorButton = document.querySelector("#previousVectorButton"),
    nextVectorButton = document.querySelector("#nextVectorButton");

const undoButton = document.querySelector("#undoButton"),
    redoButton = document.querySelector("#redoButton");

let photoTitle = document.querySelector("#photoTitle"),
    maskName = document.querySelector("#maskName");

/* Button functions */
appMinimizeButton.addEventListener('click', () => {
    BrowserWindow.getFocusedWindow().minimize();
});

appCloseButton.addEventListener('click', () => {
    BrowserWindow.getFocusedWindow().close();
});

loadImageButton.addEventListener('click', () => {
    dialog.showOpenDialog({
        title: "Load image"
    }).then(result => {
        if(fs.existsSync(result.filePaths[0])) {
            canvas.loadImage(result.filePaths[0]);

            for(var i = 0; i < 10; i++) {
                canvas.addLayer(colors[i]);
                canvas.createPolygon();
            }

            canvas.setActiveLayer(0);
            canvas.addCanvasListeners();
            setPhotoTitle();
            setCurrentMaskName();
        };
    });
});

saveLocallyButton.addEventListener('click', () => {
    if(canvas.isImageLoaded()) {
        dialog.showOpenDialog({
            title: "Choose folder to save files",
            properties: ['openDirectory']
        }).then(result => {
            const srcPath = result.filePaths[0];
            const fileSrc = canvas.canvasMainLayer.toDataURL('image/jpg', 1.0);

            var name = canvas.currentImage.src.split("/").pop().split('.')[0];
            const base64Data = fileSrc.replace(/^data:image\/png;base64,/, "");


            fs.writeFile(`${srcPath}/${name}.png`, base64Data, 'base64', (err) => {
            }); 
        
            var allMasksData = {
            };
        
            canvas.layers.forEach(layer => {
                let vector = [];
                
                layer.polygon.points.forEach(point => {
                    var pair = [Math.round(point.x), Math.round(point.y)];
                    vector.push(pair);
                });
        
                allMasksData[layer.layerName] = vector;
            });
        
            fs.writeFile(`${srcPath}/${name}.json`, JSON.stringify(allMasksData), (err) => {
            });
        });
    }
});

previousVectorButton.addEventListener('click', () => {
    var layerID = canvas.activeLayerID + -1;

    if(layerID < 0) {
        layerID = 0;
    }

    canvas.setActiveLayer(layerID);
    setCurrentMaskName();
});

nextVectorButton.addEventListener('click', () => {
    var layerID = canvas.activeLayerID + 1;

    if(layerID > 9) {
        layerID = 9;
    }

    canvas.setActiveLayer(layerID);
    setCurrentMaskName();
});

undoButton.addEventListener('click', () => {
    canvas.undo();
});

redoButton.addEventListener('click', () => {
    canvas.redo();
});

function setCurrentMaskName() {
    maskName.innerHTML = canvas.activeLayer.layerName;
}

function setPhotoTitle() {
    photoTitle.innerHTML = canvas.currentImage.src.split("/").pop();
}