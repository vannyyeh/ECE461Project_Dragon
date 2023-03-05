const path = require('path');

module.exports = {
	entry: path.resolve(__dirname, './src/index.js'),
	module: {
		rules: [
			{
				test: /\.(js|jsx)$/,
				exclude: /node_modules/,
				use: ['babel-loader'],
			},
			{
				test: /\.(jpg|png)$/,
				use: {
					loader: 'url-loader',
				},
			},
			{
				test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
				use: [
					{
						loader: 'file-loader',
					},
				],
			},
			{
				test: /\.css$/i,
				use: ['style-loader', 'css-loader'],
			},
		],
	},
	resolve: {
		extensions: ['*', '.js', '.jsx'],
	},
	output: {
		path: path.resolve(__dirname, './public'),
		filename: 'bundle.js',
		publicPath: '/',
	},
};
