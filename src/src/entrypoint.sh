#!/bin/sh

set -e

ROOT_DIR=/usr/share/nginx/html

echo "Replacing env constants in JS"
for file in $ROOT_DIR/js/app.*.js $ROOT_DIR/*.html;
do
  echo "Processing $file ...";
  sed -i 's|API_URL_PRODUCTION|'${API_URL}'|g' $file
  sed -i 's|APP_HOST_PRODUCTION|'${APP_HOST}'|g' $file
  sed -i 's|OIDC_DOMAIN_PRODUCTION|'${OIDC_DOMAIN}'|g' $file
  sed -i 's|OIDC_CLIENT_ID_PRODUCTION|'${OIDC_CLIENT_ID}'|g' $file
done

exec "$@"