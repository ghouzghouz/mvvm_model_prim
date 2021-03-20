class Notification:

    def __init__(self, MESSAGE_CONTENT, JSON_FORMAT):
        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = 'The contents of {textfile}'
        msg['From'] = me
        msg['To'] = you

    def get_message(self):

    def json_message(self):

    def send(self):
        # Send the message via our own SMTP server.
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()

    def load_info(self):

        # If we want to print a preview of the message content, we can extract whatever
        # the least formatted payload is and print the first three lines.  Of course,
        # if the message has no plain text part printing the first three lines of html
        # is probably useless, but this is just a conceptual example.
        simplest = msg.get_body(preferencelist=('plain', 'html'))
        print()
        print(''.join(simplest.get_content().splitlines(keepends=True)[:3]))

        ans = input("View full message?")
        if ans.lower()[0] == 'n':
            sys.exit()

        # We can extract the richest alternative in order to display it:
        richest = msg.get_body()
        partfiles = {}
        if richest['content-type'].maintype == 'text':
            if richest['content-type'].subtype == 'plain':
                for line in richest.get_content().splitlines():
                    print(line)
                sys.exit()
            elif richest['content-type'].subtype == 'html':
                body = richest
            else:
                print("Don't know how to display {}".format(richest.get_content_type()))
                sys.exit()
        elif richest['content-type'].content_type == 'multipart/related':
            body = richest.get_body(preferencelist=('html'))
            for part in richest.iter_attachments():
                fn = part.get_filename()
                if fn:
                    extension = os.path.splitext(part.get_filename())[1]
                else:
                    extension = mimetypes.guess_extension(part.get_content_type())
                with tempfile.NamedTemporaryFile(suffix=extension, delete=False) as f:
                    f.write(part.get_content())
                    # again strip the <> to go from email form of cid to html form.
                    partfiles[part['content-id'][1:-1]] = f.name
        else:
            print("Don't know how to display {}".format(richest.get_content_type()))
            sys.exit()
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
            # The magic_html_parser has to rewrite the href="cid:...." attributes to
            # point to the filenames in partfiles.  It also has to do a safety-sanitize
            # of the html.  It could be written using html.parser.
            f.write(magic_html_parser(body.get_content(), partfiles))
        webbrowser.open(f.name)
        os.remove(f.name)
        for fn in partfiles.values():
            os.remove(fn)
