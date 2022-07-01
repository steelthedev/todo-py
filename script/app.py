import json
import asyncio
from xml.dom.minidom import Element
from pyodide.http import pyfetch
from pyodide import JsException,create_proxy
import js


async def GetTasks():
    response = await pyfetch(
        url="http://127.0.0.1:8000/",
        method="GET",
        headers={"Content-Type": "application/json"},
    )
    if response.ok:
        data = await response.json()
        return data


async def create(e):
    task = js.document.querySelector('#taskadd').value
    js.console.log(task)
    response = await pyfetch(
        url=f"http://127.0.0.1:8000/",
        method="POST",
        headers={"Content-Type": "application/json"},
        body = json.dumps({
            "task":task
        })
    )
    if response.ok:
        data = await response.json()
        return data
    

async def delete(e):
    id = e.target.value
    response = await pyfetch(
        url=f"http://127.0.0.1:8000/delete/{id}",
        method="DELETE",
        headers={"Content-Type": "application/json"},
        verify=False
    )
    if response.ok:
        data = await response.json()
        return data


  
       