const { merge } = require('webpack-merge');
const common = require('./webpack.common.js');
const path = require('path');

module.exports = merge(common, {
    mode: 'development',
    devtool: 'inline-source-map',
	devServer: {
		static: path.resolve(__dirname, './public'),
		historyApiFallback: true,
		proxy: {
			'/api': {
				target: 'http://127.0.0.1:8000',
				secure: false,
			},
		},
	},
});
