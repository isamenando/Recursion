# Recursively count the levels of nesting for a specific document ID
def count_nested_levels(nested_documents, target_document_id, level=1):
    for document_id in nested_documents:
        # Check if the current document ID matches the target
        if document_id == target_document_id:
            return level
        # Recur into the nested documents
        # If found in deeper level, return that level
        # Otherwise, continue searching
        found_level = count_nested_levels(
            nested_documents[document_id], target_document_id, level + 1
        )
        if found_level != -1:
            return found_level
    # If the document ID is not found at this level or deeper, return -1
    return -1