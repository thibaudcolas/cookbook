#!/usr/bin/env bash

if [ -n "$JS_STAGED" ];
then
  npx eslint $JS_STAGED
fi

if [ -n "$CSS_STAGED" ];
then
  npx stylelint $CSS_STAGED
fi

PHP_STAGED=$(grep -E '.php$' <<< "$STAGED" || true)

if [ -n "$PHP_STAGED" ];
then
  php -l $PHP_STAGED
fi
