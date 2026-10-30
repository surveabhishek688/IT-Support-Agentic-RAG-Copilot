# from app.core.config import get_settings
# from app.services.ingestion import load_file,chunk_documents
# from app.rag.vectorstore import add_documents
# from pathlib import Path
#
# settings=get_settings()
#
# print(f"App Name: {settings.app_name}")
#
# docs=load_file(Path("data/sample_kb/company_it_handbook.md"))
# print(docs)
# chunks=chunk_documents(docs)
# print(len(chunks))
#
# add_documents(chunks)
#
#
#
#

import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8080, reload=True)
