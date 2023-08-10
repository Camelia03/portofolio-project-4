const deleteConfirmModal = document.getElementById('deleteConfirmModal')
if (deleteConfirmModal) {
  deleteConfirmModal.addEventListener('show.bs.modal', event => {
    // Button that triggered the modal
    const button = event.relatedTarget
    // Extract info from data-bs-post-id
    const postId = button.getAttribute('data-bs-post-id')

    // Update the form's input value
    postIdInput = deleteConfirmModal.querySelector('#postId')
    postIdInput.value = postId
  })
}