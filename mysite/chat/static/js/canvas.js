// Looks like functions are executing because console messages are printing
// Doesn't actually print out the output

window.addEventListener("load", () => {
    // Gets the canvas
    const canvas = document.querySelector(".canvas");
    // Defines what context were working in
    const ctx = canvas.getContext("2d");
  
    // Programmatically resizes to the window
    canvas.height = window.innerHeight;
    canvas.width = window.innerWidth;
  
    // Flag that indicates when you are drawing or not
    let drawing = false;
  
    // Start drawing
    function startDrawing(e){
      drawing = true;
      draw(e);
      console.log("start drawing");
    }
  
    // Stop drawing
    function endDrawing(){
      drawing = false;
      ctx.beginPath();
      console.log("stop drawing");
    }
  
    function draw(e){
      if(!drawing) return;
  
      // Style the default tool - black & circular
      //ctx.strokeStyle = "black";
      ctx.lineWidth = 10;
      ctx.lineCap = "round";
  
      // Start moving the position
      ctx.lineTo(e.clientX,e.clientY);
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(e.clientX,e.clientY);
      console.log("drawing.....");
    }
  
    // Listen for a mouse click & release
    canvas.addEventListener("mousedown", startDrawing);
    canvas.addEventListener("mouseup", endDrawing);
    canvas.addEventListener("mousemove", draw);
  });



