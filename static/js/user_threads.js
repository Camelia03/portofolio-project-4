const deleteConfirmModal = document.getElementById('deleteConfirmModal')
if (deleteConfirmModal) {
  deleteConfirmModal.addEventListener('show.bs.modal', event => {
    // Button that triggered the modal
    const button = event.relatedTarget
    // Extract info from data-bs-thread-id
    const threadId = button.getAttribute('data-bs-thread-id')

    // Update the form's input value
    const threadIdInput = deleteConfirmModal.querySelector('#threadId')
    threadIdInput.value = threadId
  })
}