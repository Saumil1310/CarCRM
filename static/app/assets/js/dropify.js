$('.dropify').dropify();

    $("body").on("click",".btn-duplicator", clone_model);
    $("body").on("click",".btn-remove", remove);

    //Functions
    function clone_model() {
      var b = $(this).parent(".duplicateable-content"),
          c = $(".model").clone(true, true);

      c.removeClass('model');
      c.find('input').addClass('dropify');

      $(b).before(c);
      $('.dropify').dropify();
    }

    function remove() {
      $(this).closest('.duplicateable-content').remove();
    }
