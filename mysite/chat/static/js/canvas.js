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
      boardSocket.send(JSON.stringify(start));
      //console.log("command -> startDrawing");
    }
  
    // Stop drawing
    function endDrawing(){
      drawing = false;
      ctx.beginPath();
      current_function = "endDrawing";
      //Handling the click event
      console.log("coordinate-end sent: " + JSON.stringify(start))
      boardSocket.send(JSON.stringify(start));
      //console.log("command -> endDrawing");
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
      //console.log("start: " + JSON.stringify(start))

      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(e.clientX,e.clientY);

      // Record end coordinates
      end.x = e.clientX;
      end.y = e.clientY;
 
      // Tell other users to start drawing
      current_function = "draw";
      //Handling the click event
      console.log("coordinates sent: " + JSON.stringify(start))
      boardSocket.send(JSON.stringify(start));
      //console.log('command -> draw')
    }
  
    // Listen for a mouse click & release
    canvas.addEventListener("mousedown", startDrawing);
    canvas.addEventListener("mouseup", endDrawing);
    canvas.addEventListener("mousemove", draw);

  });

    /* ========= Chat Function ========= */

    //boardSocket.onmessage = function(e) {
//        var data = JSON.parse(e.data);
//        var command = data['command'];
//        console.log("command: " + command);
//       
//        document.querySelector('#canvas').value += (command);
//    };

//    boardSocket.onclose = function(e) {
//        console.error('Chat for canvas socket closed unexpectedly');
//    };

//    document.querySelector('#canvas').focus();
//    document.querySelector('#canvas').onkeyup = function(e) {
//        if (e.keyCode === 13) {  // enter, return
//            document.querySelector('#canvas').onmessage();
//        }
//    };

//    document.querySelector('#canvas').onclick = function(e) {
        // Listen for a mouse click & release
//        var messageInputDom = document.querySelector('canvas');
//       var command = messageInputDom.value;
//        console.log("Message Input DOM: " + JSON.stringify(command));
//        boardSocket.send(JSON.stringify({
//            'command': command
//        }));

//        messageInputDom.value = '';
//    };
//});

