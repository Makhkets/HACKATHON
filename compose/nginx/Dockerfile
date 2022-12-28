FROM nginx
ADD ./.envs/cert.pem /etc/ssl/certs/cert.pem
ADD ./.envs/key.pem /etc/ssl/certs/key.pem
CMD ["nginx", "-g", "daemon off;"]
