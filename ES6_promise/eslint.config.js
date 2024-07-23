// eslint.config.js
const { FlatCompat } = require('@eslint/eslintrc');
const { configs: eslintRecommended } = require('@eslint/js');
const jestRecommended = require('eslint-plugin-jest').configs.recommended;

const compat = new FlatCompat({
  baseDirectory: __dirname,
  recommendedConfig: eslintRecommended.recommended,
});

module.exports = [
  ...compat.extends('eslint:recommended'),
  ...compat.extends('plugin:jest/recommended'),
  {
    files: ['**/*.js'],
    languageOptions: {
      ecmaVersion: 2018,
      sourceType: 'module',
      globals: {
        Atomics: 'readonly',
        SharedArrayBuffer: 'readonly',
        browser: true,
        es2021: true,
        jest: true,
      },
    },
    plugins: {
      jest: require('eslint-plugin-jest'),
    },
    rules: {
      'no-console': 'off',
      'no-shadow': 'off',
      'no-restricted-syntax': [
        'error',
        'LabeledStatement',
        'WithStatement',
      ],
    },
    settings: {
      jest: {
        version: 26,
      },
    },
  },
];
