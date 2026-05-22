"""
Big Brother Discord Bot
Authors: WeatherWorks
"""

import os
import asyncio
from contextlib import asynccontextmanager

from core import discord

from logging import getLogger, Logger

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, HTMLResponse
from contextlib import asynccontextmanager

from config import BASE_DIR

logger: Logger = getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
	await discord.init_discord_bot()
	
	yield

	logger.info("Succesfully shut down the Jumpstart application!")

app: FastAPI = FastAPI(docs_url="/swag",lifespan=lifespan)

if os.path.exists(os.path.join(BASE_DIR, "docs")):
	logger.info("Documentation directory found, setting up documentation endpoint!")

	app.mount(
		"/docs", StaticFiles(directory=os.path.join(BASE_DIR, "docs")), name="docs"
	)

	@app.get("/docs", include_in_schema=False)
	async def docs_redirect():
		# Mkdocs links dynamically and not being on the direct index.html causes issues
		return RedirectResponse(url="/docs/index.html")

else:
	logger.warning("Documentation directory not found, skipping documentation setup!")

logger.info("Finished setting up the application!")
@app.get("/", response_class=RedirectResponse)
async def read_index(request: Request):
	return RedirectResponse(url="/docs/index.html")
