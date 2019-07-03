#!/usr/bin/env bash

TRAVIS_STAGED=$(grep -E '.travis.(yml|yaml)$' <<< "$STAGED" || true)

if [ -n "$TRAVIS_STAGED" ];
then
  travis lint --exit-code $TRAVIS_STAGED
fi
