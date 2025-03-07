add-submodule:
	git submodule add https://github.com/huuthonguyen76/website_parser.git website_parser

update-submodule:
	git submodule update --remote --merge

run:
	python3 -m agent_playground.app.app
