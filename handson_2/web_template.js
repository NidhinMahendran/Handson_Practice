$('#submitButton').on('click',function(){
    var name  = $('#name').val()
    $("#html_remove").empty()
    $("#html_replace").html(`
        <h1 class="fst-italic lh-1 mb-4">Hello ${name}</h1>
        <p class="mb-5">You will receive a Call Shortly from our executives!,Thank you for contacting us</p>
    `)
})