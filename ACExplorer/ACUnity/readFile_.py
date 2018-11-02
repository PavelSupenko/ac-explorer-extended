import sys


def readFile(app, fileID, forgeFile=None, datafileID=None):
	data = app.tempNewFiles.getData(fileID, forgeFile, datafileID)
	if data is None:
		raise Exception('issue getting file "{}"'.format(fileID))
	
	if data['fileType'] == '415D9568':	#mesh (textures looked up)
		app.log.info(__name__, 'Exporting '.format(data['fileName']))
		app.gameFunctions.export_obj(app, fileID)
	elif data['fileType'] == 'AC2BBF68': #datablock (includes world data)
		app.gameFunctions.exportDataBlockModels(app, fileID)
	elif data['fileType'] == 'A2B7E917': #texture
		app.gameFunctions.export_texture(app, fileID)
	elif data['fileType'] == '85C817C3': #material (containing textures)
		textureIDs = app.gameFunctions.get_material_ids(app, fileID)
		if textureIDs == None:
			return
		else:
			for hexid in textureIDs:
				app.gameFunctions.export_texture(app, textureIDs[hexid])
	elif data['fileType'] =='C69A7F31':	#fakes
		app.gameFunctions.export_fakes(app, fileID)
	else:
		if app.dev:
			reload(app.gameFunctions.formatFile)  # for development
		app.gameFunctions.formatFile.topLevelFormat(app, fileID)
