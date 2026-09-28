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
			['OS=="linux"', { 'libraries': ["-Wl,-rpath,'$$ORIGIN/../../node_modules/@node-3d/deps-qt-core/<(bin)'", '<(dep_bin)/libQt6Core.so.6'] }],
			['OS=="mac"', { 'libraries': ['-Wl,-rpath,@loader_path/../../node_modules/@node-3d/deps-qt-core/<(bin)', '<(dep_bin)/QtCore.framework/Versions/A/QtCore'] }],
			['OS=="win"', { 'libraries': ['Qt6Core.lib'] }],
		],
	}],
}
