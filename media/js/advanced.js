/* This file is part of the plan timetable generator, see LICENSE for details. */

// TODO: use http://www.hunlock.com/blogs/Totally_Pwn_CSS_with_Javascript instead

(function() {
  function add_hidden_to_lectures() {
      var input = $(this);

      if (input.is(':checked')) {
          $('.lecture-' + input.val()).addClass('hide');
      } else {
          $('.lecture-' + input.val()).removeClass('hide');
      }
  };

  function add_delete_to_courses() {
      var input = $(this);

      if (input.is(':checked')) {
          $('.course-' + input.val()).addClass('delete');
      } else {
          $('.course-' + input.val()).removeClass('delete');
      }
  };

  function add_toggle() {
    var div = $(this);
    var wrapper = $('#toogle-template').clone();
    var all = wrapper.find('.toogle-all');
    var none = wrapper.find('.toogle-none');

    wrapper.removeAttr('id');
    wrapper.removeAttr('style');
    div.append(wrapper);

    none.click(function() { div.find(':checkbox').removeAttr('checked'); return false; });
    all.click(function() { div.find(':checkbox').attr('checked', 'checked'); return false; });
  }

  $(function() {
    $('#lectures input[name=exclude]:checked').each(add_hidden_to_lectures);
    $('#lectures input[name=exclude]').click(add_hidden_to_lectures);
    $('#courses input[name=course_remove]:checked').each(add_delete_to_courses);
    $('#courses input[name=course_remove]').click(add_delete_to_courses);
    $('#change-groups div.groupbox').each(add_toggle)
  });
})();
