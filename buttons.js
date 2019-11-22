//Button that bumps the light to full intensity
var Bump = $("#bump");
Bump.click(function() {
  console.log(Bump.text());
  if(Bump.text() === "Bump") {
    $.ajax({
      url: "/bump",
      type: "post",
      success: function(response) {
        console.log(response);
        Bump.text("Bump")
      }
    })
  }
}

// Button that says "Nextcue"
var Nextcue = $("#Nextcue");
Nextcue.click(function() {
  console.log(Nextcue.text());
  if(Nextcue.text() === "Next") {
    $.ajax({
      url: "/nextCue",
      type: "post",
      success: function(response) {
        console.log(response);
        Nextcue.text("Next")
      }
    })
  }
}

//button that controls the slider
var value;
$("#slider").roundSlider({
  sliderType: "min-range",
  change: function(){
  var obj1 =  $("#slider").data("roundSlider");
  value = obj1.getValue();
  $.getJSON('/valueofslider', {
    a:value
  });
