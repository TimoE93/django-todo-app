const saveBtn = document.getElementById('save-btn');
const formDetail = document.getElementById('form-detail');
const saveSuccessful = document.getElementById('save-successful');

async function sendBtnAction(event) {
  event.preventDefault();
  saveSuccessful.classList.add('hidden');
  const formData = new FormData(formDetail);

  try {
    const response = await fetch(window.location.href, {
      method: 'POST',
      body: formData,
    });
    saveSuccessful.classList.remove('hidden');
  } catch (e) {
    console.error(e);
  }
}

saveBtn.addEventListener('click', sendBtnAction);
