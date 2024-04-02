let message_body = $('.msg_card_body');
let send_message_form = $('#send-message-form');
const USER_ID = $('#logged-in-user').val();

let loc = window.location;
let wsStart = 'ws://'; // Keep HTTPS for secure communication
let endpoint = 'ws://' + loc.host + loc.pathname;




var socket = new WebSocket(endpoint);

socket.onopen = async function (e) {
  console.log('open', e);
  send_message_form.on('submit', function (e) {
    e.preventDefault();
    let message = input_message.val();
    let send_to = get_active_other_user_id();
    let thread_id = get_active_thread_id();

    let data = {
      'message': message,
      'sent_by': USER_ID,
      'send_to': send_to,
      'thread_id': thread_id
    };
    data = JSON.stringify(data);
    socket.send(data);
    $(this)[0].reset();
  });
};

socket.onmessage = async function (e) {
  console.log('message', e);
  let data = JSON.parse(e.data);
  let message = data['message'];
  let sent_by_id = data['sent_by'];
  let thread_id = data['thread_id'];
  newMessage(message, sent_by_id, thread_id);
};

socket.onerror = async function (e) {
  console.log('error', e);
};

socket.onclose = async function (e) {
  console.log('close', e);
};
