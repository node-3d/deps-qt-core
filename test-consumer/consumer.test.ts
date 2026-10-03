import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import path from 'node:path';
import test from 'node:test';

import { bin } from '@node-3d/deps-qt-core';

const require = createRequire(import.meta.url);
const consumer = require('./build/Release/consumer.node') as { probe: (library: string) => string };

const getLibrary = (): string => {
	if (process.platform === 'win32') {
		return path.join(bin, 'Qt6Core.dll');
	}
	if (process.platform === 'darwin') {
		return path.join(bin, 'QtCore.framework', 'Versions', 'A', 'QtCore');
	}
	return path.join(bin, 'libQt6Core.so.6');
};

test('loads the Qt Core candidate runtime', () =>
	assert.match(consumer.probe(getLibrary()), /^6\./u));
