include ./.env

up:
	@docker-compose -p ${DEPLOY_STACK_NAME} up -d --build --remove-orphans

down:
	@docker-compose -p ${DEPLOY_STACK_NAME} down 

ci: down up 
