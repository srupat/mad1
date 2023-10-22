from jinja2 import Template

jnanapith_data = [{"year": 1965, "awardees":"Umesh Patwardhan", "language":"Marathi"}, {"year": 1966, "awardees":"Vedashree Patwardhan", "language":"Hindi"}, {"year": 1989, "awardees":"Srujan Patwardhan", "language":"English"}]

def main():
    template_file = open("jnanapith.html.jinja2")
    TEMPLATE = template_file.read()
    template_file.close()

    template = Template(TEMPLATE)
    content = template.render(jnanapith_data = jnanapith_data)

    my_html_document_file = open("jnanapith.html", "w")
    my_html_document_file.write(content)
    my_html_document_file.close()

if __name__ == "__main__": #checks the current scope
    main()