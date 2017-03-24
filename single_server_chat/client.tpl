<html>
  <head>
    <title>Simple Chat.</title>
  </head>
  <body>
    <h4>
      %
        {{title}}
      %
    </h4>
    <hr>
    <form action="/send_msg" method="post">
      <input name="from" type="text" placeholder="From" /> <br/>
      <input name="to" type="text" placeholder="To"/> <br/>
      <textarea name = "message" rows="4" cols="50">
        Message:
      </textarea><br/>
      <input value="Send Message" type="submit" />
    </form>
    <hr>
    <form action="/msg_history" method="get">
      <input name="src" type="text" placeholder="From" /> <br/>
      <input name="dest" type="text" placeholder="To"/> <br/>              
      <input value="See the messages" type="submit" />
    </form>
  </body>
</html>
