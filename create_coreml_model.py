import coremltools

labels = './data/classes.txt'

coreml_model = coremltools.converters.keras.convert(
	'MinimalSpellingBee.h5', 
	class_labels=labels, 
	image_input_names='input1'
)


coreml_model.author = 'Daniel Oberg'
coreml_model.license = 'MIT'
coreml_model.short_description = "Japanese Spelling Bee"

coreml_model.input_description['input1'] = 'MFCC image to be classified'

coreml_model.output_description['output1'] = 'Probability of each hiragana character in romaji, including dash and xtsu'
coreml_model.output_description['classLabel'] = 'Most likely hiragana character'

coreml_model.save('SpellingBee.mlmodel')
