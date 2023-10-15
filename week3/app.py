from jinja2 import Template


TEMPLATE = """
Hello {{name}} !
"""
# jnanapith_data = {"year":1965, "awardees": }

def main():
    template = Template(TEMPLATE)
    print(template.render(name="Srujan"))

if __name__ == "__main__":
    main()