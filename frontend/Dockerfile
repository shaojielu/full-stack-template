# Estágio 0, "build-stage", baseado em Node.js, para construir e compilar o frontend
FROM node:20 AS build-stage

WORKDIR /app

# Habilita o corepack para usar o pnpm
RUN corepack enable

# Copia os arquivos de manifesto de pacotes
COPY package.json pnpm-lock.yaml* ./

# Instala as dependências com pnpm
RUN pnpm install --frozen-lockfile

# Copia o restante dos arquivos da aplicação
COPY ./ /app/

# Define o argumento para a URL da API
ARG VITE_API_URL=${VITE_API_URL}

# Executa o build da aplicação
RUN pnpm run build


# Estágio 1, baseado em Nginx, para ter apenas o aplicativo compilado, pronto para produção com Nginx
FROM nginx:1

# Copia os arquivos compilados do estágio de build
COPY --from=build-stage /app/dist/ /usr/share/nginx/html

# Copia os arquivos de configuração do Nginx
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
COPY ./nginx-backend-not-found.conf /etc/nginx/extra-conf.d/backend-not-found.conf