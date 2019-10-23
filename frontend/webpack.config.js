const webpack = require("webpack")
const ExtractTextPlugin = require("extract-text-webpack-plugin")
const MiniCssExtractPlugin = require("mini-css-extract-plugin")

module.exports = {
    entry: "./src/index.jsx",
    output: {
        path: __dirname + "/public",
        filename: "./app.js"
    },
    devServer: {
        port: 8080,
        contentBase: "./public"
    },
    resolve: {
        extensions: [".js", ".jsx"],
        alias: {
            modules: __dirname + "/node_modules"
        }
    },
    plugins: [
        new ExtractTextPlugin("app.css")
    ],
    module: {
        rules: [
        {
            test: /.js[x]?$/,
            loader: "babel-loader",
            exclude: "/node_modules/",
            query: {
                "presets": ["@babel/preset-env","@babel/preset-react"],              
                "plugins": ["@babel/plugin-transform-object-assign"]
              
              }
              
        }, {
            test: /\.css$/,
            loader: [ 'style-loader', 'css-loader' ],
        }, {
            test: /\.woff|.woff2|.ttf|.eot|.svg*.*$/,
            loader: "file-loader"
        }, {
            test: /\.png$/,
            loader: "react-load-image"
        }]
    }
}