const deleteConfirmModal = document.getElementById('deleteConfirmModal');
if (deleteConfirmModal) {
  deleteConfirmModal.addEventListener('show.bs.modal', event => {
    // Button that triggered the modal
    const button = event.relatedTarget;
    // Extract info from data-bs-thread-id
    const replyId = button.getAttribute('data-bs-reply-id');

    // Update the form's input value
    const replyIdInput = deleteConfirmModal.querySelector('#replyId');
    replyIdInput.value = replyId;
  });
}