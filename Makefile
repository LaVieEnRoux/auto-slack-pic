clean:
	rm -f slack-pic *.pyc

install: slack-pic
	install -d /usr/local/bin/
	install -m 755 slack-pic /usr/local/bin/

uninstall:
	rm -rf /usr/local/bin/slack-pic

slack-pic: slack-pic.py
	cp slack-pic.py slack-pic
