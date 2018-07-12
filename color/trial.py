import Algorithmia
input = {
 "image": "IMAGE SRC" 
}
client = Algorithmia.client("KEY") #insert your own API key
algo = client.algo("deeplearning/ColorfulImageColorization/1.1.5")
response = algo.pipe(input)
print (response.result)