# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import asyncio
import concurrent

import aiohttp
import pytest

async def feature():
    return "Hello, Async World!"

# 1
@pytest.mark.asyncio
async def test_successful_promise_resolution(event_loop):
    result = await feature()
    assert result == "Hello, Async World!"

async def failing_feature():
    raise ValueError("Something went wrong!")

#2
@pytest.mark.asyncio
async def test_failed_promise_rejection(event_loop):
    with pytest.raises(ValueError, match="Something went wrong!"):
        await failing_feature()

async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            return await response.json()

#3
@pytest.mark.asyncio
async def test_http_request(event_loop):
    result = await fetch_data()
    assert result["userId"] == 1

async def insert_data():
    pass

#4
@pytest.mark.asyncio
async def test_database_insertion(event_loop):
    await insert_data()

async def async_function():
    return "Async Result"

def run_async_function_in_thread():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(async_function())
    loop.close()
    return result

#5
@pytest.mark.asyncio
async def test_run_async_function_in_thread(event_loop):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = await event_loop.run_in_executor(executor, run_async_function_in_thread)
    assert result == "Async Result"