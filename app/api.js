const endpoint = "https://isaip0v8i1.execute-api.us-east-2.amazonaws.com/api/"

async function postImage(name, image) {
	await fetch({
		body: {
			name: name,
			data: Buffer.from(image).toString("base64")
		}
	})
}