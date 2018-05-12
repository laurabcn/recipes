FROM phpdockerio/php72-fpm:latest
WORKDIR "/application"

# Install selected extensions and other stuff
RUN apt-get update \
    && apt-get -y --no-install-recommends install wget sudo php-memcached php7.2-mysql php-redis php-xdebug php7.2-intl php-mongodb php7.2-soap \
    && apt-get clean; rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*

ENV XDEBUG_ENABLE true
ENV XDEBUG_REMOTE_PORT 9001
ENV XDEBUG_REMOTE_HOST 10.254.254.254

# Install Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

WORKDIR /var/www/recipes

RUN chown -R 1000:1000 /var/www

RUN usermod -u 1000 www-data


