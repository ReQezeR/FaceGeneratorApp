class CAFECanvas {
    layers = [];
    activeLayer = null;
    activeLayerID = null;
    canvasMainLayer = null;
    canvasTempLayer = null;
    currentImage = null;
    img = null;
    transformation = {
        zoom: 1,
        position: {
            x: 0,
            y: 0
        }
    }
    maskNames = ['face', 'l_eye', 'r_eye', 'mouth', 'nose', 'l_ear', 'r_ear', 'hair', 'l_eyebrow', 'r_eyebrow'];
    mouseDown = false;
    mouseLastX = null;
    mouseLastY = null;

    constructor(canvasContainerID) {
        var self = this;

        self.canvasContainerID = canvasContainerID;
        self.canvasContainer = document.querySelector(`#${canvasContainerID}`);

        self._setupCanvasContainer();
        
        if(!self.canvasContainer) {
            self._printError('Couldn\'t find canvas with given id!');
        }
    }

    _setupCanvasContainer() {
        var self = this;

        var canvasContainer = self.canvasContainer;
        canvasContainer.classList.add('canvasContainer');
        
        self.canvasMainLayer = document.createElement('canvas');
        self.canvasMainLayer.width = 480;
        self.canvasMainLayer.height = 480;
        self.canvasMainLayer.id = 'canvasMainLayer';

        self.canvasTempLayer = document.createElement('canvas');
        self.canvasTempLayer.width = 480;
        self.canvasTempLayer.height = 480;
        self.canvasTempLayer.id = 'canvasTempLayer';

        canvasContainer.appendChild(self.canvasMainLayer);
        canvasContainer.appendChild(self.canvasTempLayer);
    }

    loadImage(imgSrc) {
        var self = this;
        
        if(self.canvasMainLayer) {
            self.currentImage = new Image();

            self.currentImage.addEventListener('load', function() {
                let ctx = self.canvasMainLayer.getContext('2d');

                self._drawImageProp(ctx, self.currentImage);
            }, false);

            self.currentImage.src = imgSrc;
        } else {
            self._printError('There is no canvas assigned!');
        }
    }

    addLayer(color) {
        var self = this;

        var canvas = document.createElement('canvas');
        canvas.width = 480;
        canvas.height = 480;
        canvas.id = `canvasLayer--${self.layers.length + 1}`;      

        self.canvasContainer.appendChild(canvas);

        var layer = {
            canvas: canvas,
            polygon: null,
            layerName: self.maskNames.shift(),
            color
        };

        self.layers.push(layer);
        self.activeLayer = layer;
        self.activeLayerID = self.layers.length - 1;
    }

    createPolygon() {
        var self = this;

        if(self.activeLayer) {
            var polygon = {
                color: self.activeLayer.color,
                points: [],
                historyPoints: []
            }

            self.activeLayer.polygon = polygon;
        } else {
            self._printError('There is no layer selected!');
        }
    }

    setActiveLayer(layerID) {
        var self = this;

        self.activeLayer = self.layers[layerID];
        self.activeLayerID = layerID;
    }

    addCanvasListeners() {
        var self = this;

        // Following dot
        self.canvasContainer.addEventListener('mousemove', (event) => {
            var canvasTempLayer = canvas.canvasTempLayer;
            var ctx = canvasTempLayer.getContext('2d');
            ctx.clearRect(0, 0, canvasTempLayer.width, canvasTempLayer.height);
        
            var rect = canvasTempLayer.getBoundingClientRect();
            var x = event.clientX - rect.left;
            var y = event.clientY - rect.top;
        
            ctx.beginPath();
            ctx.arc(x, y, 3, 0, 2 * Math.PI, true);
            ctx.fill();
        });

        // Adding points
        self.canvasContainer.addEventListener('click', (event) => {    
            if(self.activeLayer && !event.altKey) {
                var layer = self.activeLayer;
                var canvas = layer.canvas;
                var ctx = canvas.getContext('2d');
                ctx.clearRect(0, 0, canvasTempLayer.width, canvasTempLayer.height);
        
                let x = event.layerX;
                let y = event.layerY;

                x = (-self.transformation.position.x + x) / self.transformation.zoom;
                y = (-self.transformation.position.y + y) / self.transformation.zoom;

                var points = layer.polygon.points;
        
                points.push({x: x, y: y});
                self._drawPolygons();
                layer.historyPoints = [];
            }
        });

        // Scrolling
        self.canvasContainer.addEventListener('wheel', (event) => {
            let ctx = self.canvasMainLayer.getContext('2d');
            const tempZoom = self.transformation.zoom;


            // Zoom in
            if(event.deltaY < 0) {
                self.transformation.zoom += 0.05;

                if(self.transformation.zoom > 3.0) {
                    self.transformation.zoom = 3.0;
                }
            } 
            // Zoom out
            else {
                self.transformation.zoom -= 0.05;

                if(self.transformation.zoom < 1.0) {
                    self.transformation.zoom = 1.0;
                }
            }

            ctx.clearRect(0, 0, self.canvasMainLayer.width, self.canvasMainLayer.height);

            const mouseX = event.layerX;
            const mouseY = event.layerY;

            const imageRealX = ((-self.transformation.position.x) + mouseX) / tempZoom;
            const imageRealY = ((-self.transformation.position.y) + mouseY) / tempZoom;

            const zoomedX = imageRealX * self.transformation.zoom;
            const zoomedY = imageRealY * self.transformation.zoom;

            let posX = mouseX - zoomedX;
            let posY = mouseY - zoomedY;

            if(posX > 0) {
                posX = 0;
            }

            if(posX + 480 * self.transformation.zoom < 480) {
                posX = 480 * self.transformation.zoom - 480;
            }

            if(posY > 0) {
                posY = 0;
            }

            if(posY + 480 * self.transformation.zoom < 480) {
                posY = 480 * self.transformation.zoom - 480;
            }


            self.transformation.position.x = posX;
            self.transformation.position.y = posY;

            var size = Math.round(480 * self.transformation.zoom);

            self._drawImageProp(ctx, self.currentImage, self.transformation.position.x, self.transformation.position.y, size, size);
            self._drawPolygons();
        });

        // Moving
        self.canvasContainer.addEventListener('mousedown', (event) => {  
            self.mouseDown = true;
        });

        self.canvasContainer.addEventListener('mouseup', (event) => {  
            self.mouseDown = false;
            self.mouseLastX = null;
            self.mouseLastY = null;
        });    
    
        self.canvasContainer.addEventListener('mousemove', (event) => {
            if(self.mouseDown && event.altKey) {
                let ctx = self.canvasMainLayer.getContext('2d');    
                ctx.clearRect(0, 0, self.canvasMainLayer.width, self.canvasMainLayer.height);
                let size = 480 * self.transformation.zoom;

                if(self.mouseLastX === null) {
                    self.mouseLastX = event.layerX;
                } else {
                    self.transformation.position.x += event.layerX - self.mouseLastX;

                    if(self.transformation.position.x > 0) {
                        self.transformation.position.x = 0;
                    }

                    if(self.transformation.position.x + 480 * self.transformation.zoom < 480) {
                        self.transformation.position.x = 480 * self.transformation.zoom - 480;
                    }

                    self._drawImageProp(ctx, self.currentImage, self.transformation.position.x, self.transformation.position.y, size, size);
                    self._drawPolygons();
                    
                    self.mouseLastX = event.layerX;
                }

                if(self.mouseLastX === null) {
                    self.mouseLastY = event.layerY;
                } else {
                    self.transformation.position.y += event.layerY - self.mouseLastY;

                    if(self.transformation.position.y > 0) {
                        self.transformation.position.y = 0;
                    }

                    if(self.transformation.position.y + 480 * self.transformation.zoom < 480) {
                        self.transformation.position.y = 480 * self.transformation.zoom - 480;
                    }

                    self._drawImageProp(ctx, self.currentImage, self.transformation.position.x, self.transformation.position.y, size, size);
                    self._drawPolygons();

                    self.mouseLastY = event.layerY;
                }
            }
        });
    }

    /**
     * TODO: analyze this method and try to do it my way
     */
    _drawImageProp(ctx, img, x, y, w, h, offsetX, offsetY) {

        if (arguments.length === 2) {
            x = y = 0;
            w = ctx.canvas.width;
            h = ctx.canvas.height;
        }
    
        // default offset is center
        offsetX = typeof offsetX === 'number' ? offsetX : 0.5;
        offsetY = typeof offsetY === 'number' ? offsetY : 0.5;
    
        // keep bounds [0.0, 1.0]
        if (offsetX < 0) offsetX = 0;
        if (offsetY < 0) offsetY = 0;
        if (offsetX > 1) offsetX = 1;
        if (offsetY > 1) offsetY = 1;
    
        var iw = img.width,
            ih = img.height,
            r = Math.min(w / iw, h / ih),
            nw = iw * r,   // new prop. width
            nh = ih * r,   // new prop. height
            cx, cy, cw, ch, ar = 1;
    
        // decide which gap to fill    
        if (nw < w) ar = w / nw;                             
        if (Math.abs(ar - 1) < 1e-14 && nh < h) ar = h / nh;  // updated
        nw *= ar;
        nh *= ar;
    
        // calc source rectangle
        cw = iw / (nw / w);
        ch = ih / (nh / h);
    
        cx = (iw - cw) * offsetX;
        cy = (ih - ch) * offsetY;
    
        // make sure source rectangle is valid
        if (cx < 0) cx = 0;
        if (cy < 0) cy = 0;
        if (cw > iw) cw = iw;
        if (ch > ih) ch = ih;
    
        // fill image in dest. rectangle
        ctx.drawImage(img, cx, cy, cw, ch, x, y, w, h);
    }

    _drawPolygons() {
        let self = this;

        const moveX = self.transformation.position.x;
        const moveY = self.transformation.position.y;
        const zoom = self.transformation.zoom;

        self.layers.forEach((layer) => {
            if(layer.polygon.points.length > 0) {

                var canvas = layer.canvas;

                canvas.width = 480 * zoom;
                canvas.height = 480 * zoom;

                canvas.style.left = `${moveX}px`;
                canvas.style.top = `${moveY}px`;

                var ctx = canvas.getContext('2d');

                var points = layer.polygon.points;
            
                ctx.beginPath();
                ctx.arc(points[0].x * zoom, points[0].y * zoom, 3, 0, 2 * Math.PI, true);
                ctx.moveTo(points[0].x * zoom , points[0].y * zoom);
        
                for(var i = 1; i < points.length; i++) {
                    ctx.arc(points[i].x * zoom, points[i].y * zoom, 3, 0, 2 * Math.PI, true);
                    ctx.lineTo(points[i].x * zoom, points[i].y * zoom);
                }
                
                ctx.closePath();
                ctx.stroke();
                ctx.globalAlpha = 0.2;
                ctx.fillStyle = layer.color;
                ctx.fill();
            }
        });
    }

    undo() {
        const self = this;

        const activeLayer = self.activeLayer;

        if(activeLayer.polygon.points.length > 0) {
            activeLayer.polygon.historyPoints.push(activeLayer.polygon.points.pop());
            self._drawPolygons();
        }
    }
    
    redo() {
        const self = this;

        const activeLayer = self.activeLayer;
        if(activeLayer.polygon.historyPoints.length > 0) {
            activeLayer.polygon.points.push(activeLayer.polygon.historyPoints.pop());
            self._drawPolygons();
        }
    }

    isImageLoaded() {
        var self = this;

        if(!self.currentImage) {
            return false;
        }

        return true;
    }

    _printError(message) {
        console.error(`[CAFE][Canvas] Error! ${message}`);
    }
}