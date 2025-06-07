from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission


@tool(
    name="ContentExtractorByUrl",
    description="Extract content from a URL",
    permission=ToolPermission.READ_ONLY,
)
def content_extractor_by_url(url: str) -> str:
    """
    Extract content from a URL.

    :param url: The URL to extract content from.
    :returns: The extracted content.
    """
    from docling.document_converter import DocumentConverter

    try:
        converter = DocumentConverter()
        conversion_result = converter.convert(source=url)
        markdown = conversion_result.document.export_to_markdown(image_placeholder="")
        return markdown
    except Exception as e:
        return str(e)
