{
	'variables': {
		'dep_bin': '<!(node -p "require(\'@node-3d/deps-qt-core\').bin")',
		'bin': '<!(node -p "require(\'@node-3d/addon-tools\').getBin()")',
	},
	'targets': [{
		'target_name': 'consumer',
		'sources': ['consumer.cpp'],
		'library_dirs': ['<(dep_bin)'],
		'conditions': [
			['OS=="linux"', { 'libraries': [
				"-Wl,-rpath,'$$ORIGIN/../../node_modules/@node-3d/deps-qt-core/<(bin)'",
				'-Wl,--no-as-needed',
				'<(dep_bin)/libicudata.so.73',
				'<(dep_bin)/libicui18n.so.73',
				'<(dep_bin)/libicuio.so.73',
				'<(dep_bin)/libicutest.so.73',
				'<(dep_bin)/libicutu.so.73',
				'<(dep_bin)/libicuuc.so.73',
				'<(dep_bin)/libQt6Core.so.6',
				'<(dep_bin)/libQt6DBus.so.6',
				'<(dep_bin)/libQt6Network.so.6',
				'-Wl,--as-needed',
			] }],
			['OS=="mac"', { 'libraries': [
				'-Wl,-rpath,@loader_path/../../node_modules/@node-3d/deps-qt-core/<(bin)',
				'<(dep_bin)/QtCore.framework/Versions/A/QtCore',
				'<(dep_bin)/QtDBus.framework/Versions/A/QtDBus',
				'<(dep_bin)/QtNetwork.framework/Versions/A/QtNetwork',
			] }],
			['OS=="win"', { 'libraries': ['Qt6Core.lib'] }],
		],
	}],
}
