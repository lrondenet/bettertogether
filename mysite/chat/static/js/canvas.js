// Looks like functions are executing because console messages are printing
// Doesn't actually print out the output

window.addEventListener("load", () => {
    // Gets the canvas
    const canvas = document.querySelector("#canvas");
    // Defines what context were working in
    const ctx = canvas.getContext("2d");
 
    // Holds start & end positions
    var start = {};
    var end = {};
    var plots = [];

    // Tracks currently executing function
    var current_function = '';

    // Programmatically resizes to the window
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;
  
    // Flag that indicates when you are drawing or not
    let drawing = false;
  
    // Start drawing
    function startDrawing(e){
      drawing = true;
      draw(e);
      current_function = "startDrawing";
      //Handling the click event
      console.log("coordinate-start sent: " + JSON.stringify(start))
      //console.log("command -> startDrawing");
    }
  
    // Stop drawing
    function endDrawing(){
      drawing = false;
      ctx.beginPath();
      current_function = "endDrawing";
      //Handling the click event
      console.log("coordinate-end sent: " + JSON.stringify(start))
      //console.log("command -> endDrawing");
      console.log("coordinates sent: " + JSON.stringify(plots))
      /*boardSocket.send(JSON.stringify({
        'coordinates': coords
      }));*/
    }
  
    function draw(e){
      if(!drawing) return;
  
      // Style the default tool - black & circular
      ctx.lineWidth = 10;
      ctx.lineCap = "round";
  
      // Start moving the position
      ctx.lineTo(e.clientX,e.clientY);
      
      // Record starting coordinates
      start.x = e.clientX;
      start.y = e.clientY;
      storeCoordinate(start.x, start.y, plots);
      //console.log("start: " + JSON.stringify(start))

      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(e.clientX,e.clientY);
      storeCoordinate(e.clientX,e.clientY, plots);

      // Record end coordinates
      end.x = e.clientX;
      end.y = e.clientY;
      storeCoordinate(end.x, end.y, plots);
  
 
      // Tell other users to start drawing
      current_function = "draw";
      //Handling the click event
      //console.log('command -> draw')
    }
  
    // Listen for a mouse click & release
    canvas.addEventListener("mousedown", startDrawing);
    canvas.addEventListener("mouseup", endDrawing);
    canvas.addEventListener("mousemove", draw);

    function storeCoordinate(xVal, yVal, array) {
      array.push({x: xVal, y: yVal});
    }

    /* PUBNUB MULTIUSER CHAT API */
    var channel = 'my-draw-demo';

    var pubnub = PUBNUB.init({
    //var pubnub = new PubNub({
      publish_key: "pub-c-e77bd0c0-5551-48fd-900b-0528b548d2a3",
      subscribe_key: "sub-c-f3c4a864-170f-11ea-a1d5-ea5a03b00545",
      ssl: true
    });

    pubnub.publish({
      'channel': channel,
      'message': { 
        'plots': plots // your array goes here
      } 
    });

    pubnub.subscribe({
      channel: channel,
      callback: drawFromStream,

      // Add presence
      presence: function(m){
        var element = document.getElementById('occupancy');
        if(element){
          element.textContent = m.occupancy;
        }
      }
    });

    function drawOnCanvas(color, plots) {
      ctx.beginPath();
      ctx.moveTo(plots[0].x, plots[0].y);
    
      for(var i=1; i<plots.length; i++) {
        ctx.lineTo(plots[i].x, plots[i].y);
      }
      ctx.stroke();
    }

    function drawFromStream(message) {
      if(!message) return;        
  
      ctx.beginPath();
      drawOnCanvas(message.plots);
    }
    /* END PUBNUB MULTIUSER CHAT API */
});