NAME = ft_linear_regression
PYTHON = python3

# Generated/artifact files
GENERATED = thetas.json precision.json visualisation.png
CACHE = __pycache__ .*.pyc *.pyc

GREEN = \033[0;32m
RED = \033[0;31m
YELLOW = \033[0;33m
NC = \033[0m

all: train
	@echo "$(GREEN)✅ $(NAME) ready. Use 'make bonus', 'make predict', 'make clean' or 'make fclean'.$(NC)"

train:
	@echo "$(GREEN)Training $(NAME)...$(NC)"
	$(PYTHON) ft_training.py

predict:
	@echo "$(GREEN)Running prediction (interactive)...$(NC)"
	$(PYTHON) ft_prediction.py

bonus:
	@echo "$(GREEN)Running bonus (precision + visualization)...$(NC)"
	$(PYTHON) ft_bonus.py

clean:
	@echo "$(RED)Cleaning cache...$(NC)"
	@rm -rf __pycache__
	@find . -maxdepth 1 -name "*.pyc" -delete 2>/dev/null || true

fclean: clean
	@echo "$(RED)Cleaning generated files...$(NC)"
	@rm -f $(GENERATED)

re: fclean all

.PHONY: all train predict bonus clean fclean re
