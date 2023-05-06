import cohere

# Replace 'YOUR_API_KEY' with your actual API key
co = cohere.Client('3pbIU5yOhATFLrAS7eSOCVE8M7N0YhPrIIijXOfO')

# Get input from user
prompt = input('Enter your prompt: ')

# Generate response using Cohere API
response = co.generate(
  model='command-xlarge-nightly',
  prompt=prompt,
  max_tokens=300,
  temperature=0.9,
  k=0,
  stop_sequences=[],
  return_likelihoods='NONE')

# Print generated response
print('Response: {}'.format(response.generations[0].text))
