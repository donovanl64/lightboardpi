var bump = $("#bump");
bump.click(function() {
  console.log(bump.text());
  if(bump.text() === "Bump") {
    $.ajax({
      url: "/bump",
      type: "post",
      success: function(response) {
        console.log(response);
        redbutton.text("Bump")
      }
    })
  }
}
