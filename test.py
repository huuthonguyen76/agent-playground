from website_parser.website_parser.parser.starterstory import StarterStoryParser

parser = StarterStoryParser(html_executor_url="http://localhost:8000")

print(parser.parse('https://www.starterstory.com/stories/brumate'))