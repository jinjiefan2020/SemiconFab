export default [
  {
    ignores: [
      "node_modules/**",
      ".venv/**",
      "benchmark/simulator/**",
      "tools/validator/**",
      "output/**",
      "**/*.html",
    ],
  },
  {
    files: ["js/**/*.js"],
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: {
        window: "readonly",
        document: "readonly",
        fetch: "readonly",
        console: "readonly",
        Response: "readonly",
        URL: "readonly",
      },
    },
    rules: {
      "no-undef": "off",
      "no-unused-vars": "off",
    },
  },
];
