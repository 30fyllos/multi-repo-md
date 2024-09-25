from jinja2 import Environment, FileSystemLoader
import yaml

# Load the Jinja2 template
file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)
template = env.get_template('template.yml')

# Load the repos data from repos.yml file
with open('repos.yml', 'r') as repos_file:
    repos_data = yaml.safe_load(repos_file)

# Extract the 'repos' list from the loaded YAML data
repos = repos_data['repos']

# Render the template with the loaded data
output = template.render(repos=repos)

# Save the output to mkdocs.yml file
with open('mkdocs.yml', 'w') as f:
    f.write(output)

print("YAML file generated successfully.")
