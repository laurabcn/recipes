FROM debian:jessie

ENV NGINX_VERSION 1.13.0-1~jessie

RUN apt-get update

RUN apt-key adv --keyserver-options http-proxy=$http_proxy --keyserver hkp://pgp.mit.edu:80 --recv-keys 573BFD6B3D8FBC641079A6ABABF5BD827BD9BF62
RUN echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install --no-install-recommends --no-install-suggests -y
RUN apt-get install --no-install-recommends --no-install-suggests -y ca-certificates
RUN apt-get install --no-install-recommends --no-install-suggests -y nginx=${NGINX_VERSION}
RUN apt-get install --no-install-recommends --no-install-suggests -y nginx-module-xslt
RUN apt-get install --no-install-recommends --no-install-suggests -y nginx-module-geoip
RUN apt-get install --no-install-recommends --no-install-suggests -y nginx-module-image-filter
RUN apt-get install --no-install-recommends --no-install-suggests -y nginx-module-perl
RUN apt-get install --no-install-recommends --no-install-suggests -y nginx-module-njs
RUN apt-get install --no-install-recommends --no-install-suggests -y gettext-base
RUN rm -rf /var/lib/apt/lists/*


COPY nginx.conf /etc/nginx/
COPY symfony.conf /etc/nginx/conf.d/
COPY upstream.conf /etc/nginx/conf.d/

RUN id -u www-data &>/dev/null || adduser -D -g '' -u 501 www-data www-data

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
&& ln -sf /dev/stderr /var/log/nginx/error.log

CMD ["service", "nginx", "start"]

