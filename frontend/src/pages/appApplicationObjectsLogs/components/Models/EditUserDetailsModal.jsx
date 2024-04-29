import { Dialog, Transition } from '@headlessui/react';
import { Formik } from 'formik';
import { get } from 'lodash';
import { Fragment } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom';
import * as Yup from 'yup';
import { ReactComponent as ModalCloseIcon } from '../../../../assets/images/svg/modal-close-icon.svg';
import MultiSelectField from '../../../../components/Form/MultiSelectField';
import useApi from '../../../../hooks/useApi';
import { transformToFormData } from '../../../../utils/helper';
import {
	closeIsEditUserDetailModalOpen,
	selectAppApplicationObjectsLogsData,
	selectAppApplicationObjectsLogsFormData,
	selectIsEditUserDetailModalOpen,
	toggleRerenderPage,
} from '../../slice';

const EditUserDetailsForm = ({ closeModal }) => {
	let { appId } = useParams();
	const dispatch = useDispatch();

	const appApplicationObjectsLogsData = useSelector(
		selectAppApplicationObjectsLogsData
	);
	const appApplicationObjectsLogsFormData = useSelector(
		selectAppApplicationObjectsLogsFormData
	);

	const triggerApi = useApi();
	let initialValues = {
		name: appApplicationObjectsLogsFormData?.name ?? '',
		email: appApplicationObjectsLogsFormData?.email ?? '',
		mobile: appApplicationObjectsLogsFormData?.mobile?.slice(4) ?? '',
		roles:
			appApplicationObjectsLogsFormData?.roles?.map((eachApp) => eachApp.id) ??
			[],
	};

	let validationSchema = Yup.object().shape(
		{
			name: Yup.string().required('Required'),
			email: Yup.string().when(['mobile'], {
				is: (mobile) => {
					if (!mobile) return true;
				},
				then: Yup.string().email('Invalid email address').required('Required'),
				otherwise: Yup.string(),
			}),
			mobile: Yup.string().when(['email'], {
				is: (email) => {
					if (!email) return true;
				},
				then: Yup.string()
					.min(10, 'Must be 10 digits')
					.max(10, 'Must be 10 digits')
					.required('Required'),
				otherwise: Yup.string()
					.min(10, 'Must be 10 digits')
					.max(10, 'Must be 10 digits'),
			}),
			roles: Yup.array().min(1, 'Minimun one is required').required('Required'),
		},
		[['name'], ['mobile', 'email'], ['email', 'mobile'], ['roles']]
	);

	let onSubmit = (values) => {
		let tempValues = values;

		let dynamicFormData = transformToFormData(tempValues);

		const makeApiCall = async () => {
			const { response, success } = await triggerApi({
				url: `/api/v1/apps/${appId}/users/${appApplicationObjectsLogsFormData?.id}/`,
				type: 'PUT',
				loader: true,
				payload: dynamicFormData,
			});

			if (success && response) {
				closeModal();
				dispatch(toggleRerenderPage());
			}
		};

		makeApiCall();
	};

	return (
		<Formik
			initialValues={initialValues}
			validationSchema={validationSchema}
			onSubmit={onSubmit}
		>
			{(formik) => {
				return (
					<form
						className="complete-hidden-scroll-style flex grow flex-col gap-4 overflow-y-auto"
						onSubmit={formik.handleSubmit}
					>
						<div className="flex grow flex-col gap-[16px]">
							<div className="flex flex-col gap-[4px]">
								<label
									htmlFor="name"
									className="font-lato text-form-xs font-semibold text-[#A3ABB1]"
								>
									Full Name
								</label>
								<input
									id="name"
									name="name"
									type="text"
									onChange={formik.handleChange}
									onBlur={formik.handleBlur}
									value={formik.values.name}
									className="rounded-[6px] border border-[#DDE2E5] px-[16px] py-[14px] font-lato placeholder:text-[#9A9A9A] hover:outline-0 focus:outline-0"
									placeholder="Enter full name of the user"
								/>
								{formik.touched.name && formik.errors.name ? (
									<div className="font-lato text-form-xs text-[#cc3300]">
										{formik.errors.name}
									</div>
								) : null}
							</div>
							<div className="flex flex-col gap-[4px]">
								<label
									htmlFor="email"
									className="font-lato text-form-xs font-semibold text-[#A3ABB1]"
								>
									Email
								</label>
								<input
									id="email"
									name="email"
									type="text"
									onChange={formik.handleChange}
									onBlur={formik.handleBlur}
									value={formik.values.email}
									className="rounded-[6px] border border-[#DDE2E5] px-[16px] py-[14px] font-lato placeholder:text-[#9A9A9A] hover:outline-0 focus:outline-0"
									placeholder="Enter"
								/>
								{formik.touched.email && formik.errors.email ? (
									<div className="font-lato text-form-xs text-[#cc3300]">
										{formik.errors.email}
									</div>
								) : null}
							</div>
							<div className="flex flex-col gap-[4px]">
								<label
									htmlFor="mobile"
									className="font-lato text-form-xs font-semibold text-[#A3ABB1]"
								>
									Mobile
								</label>
								<div className="flex gap-[12px] rounded-[6px] border border-[#DDE2E5] px-[12px] py-[14px]">
									<span className="font-lato text-[#6C747D]">+91</span>
									<input
										id="mobile"
										name="mobile"
										type="number"
										onChange={formik.handleChange}
										onBlur={formik.handleBlur}
										value={formik.values.mobile}
										className="font-lato placeholder:text-[#9A9A9A] hover:outline-0 focus:outline-0"
										placeholder="00000 00000"
									/>
								</div>
								{formik.touched.mobile && formik.errors.mobile ? (
									<div className="font-lato text-form-xs text-[#cc3300]">
										{formik.errors.mobile}
									</div>
								) : null}
							</div>
							<MultiSelectField
								key="roles"
								label="User Role"
								name="roles"
								id="roles"
								placeholder="Select roles"
								value={get(formik.values, 'roles', [])}
								optionsDataName="roles"
								optionsData={
									appApplicationObjectsLogsData?.dropdown_options?.roles ?? []
								}
								formik={formik}
							/>
						</div>
						<div className="sticky bottom-0 flex flex-col gap-[8px] bg-[#ffffff] pt-[24px] font-lato text-[#696969]">
							<button
								type="submit"
								className="flex w-full items-center justify-center rounded-[4px] bg-primary px-[16px] py-[10px] font-lato text-[14px] font-bold leading-[20px] text-white disabled:opacity-[0.38]"
							>
								<span>Save</span>
							</button>
						</div>
					</form>
				);
			}}
		</Formik>
	);
};

export default function EditUserDetailsModal() {
	const isEditUserDetailModalOpen = useSelector(
		selectIsEditUserDetailModalOpen
	);
	const dispatch = useDispatch();

	function closeModal() {
		dispatch(closeIsEditUserDetailModalOpen());
	}

	return (
		<>
			<Transition appear show={isEditUserDetailModalOpen} as={Fragment}>
				<Dialog as="div" className="relative z-10" onClose={() => {}}>
					<Transition.Child
						as={Fragment}
						enter="ease-in-out duration-700"
						enterFrom="opacity-0"
						enterTo="opacity-100"
						leave="ease-in-out duration-700"
						leaveFrom="opacity-100"
						leaveTo="opacity-0"
					>
						<div className="fixed inset-0 bg-black bg-opacity-[.67]" />
					</Transition.Child>

					<Transition.Child
						as={Fragment}
						enter="transform transition ease-in-out duration-500"
						enterFrom="translate-x-full"
						enterTo="translate-x-0"
						leave="transform transition ease-in-out duration-500"
						leaveFrom="translate-x-0"
						leaveTo="translate-x-full"
					>
						<div className="fixed inset-0 overflow-y-auto">
							<div className="flex h-screen max-h-screen min-h-full grow items-center justify-center text-center md:justify-end">
								<Dialog.Panel className="relative flex h-screen max-h-screen min-h-full w-full max-w-[498px] transform flex-col gap-[32px] overflow-hidden bg-white px-[24px] pt-[52px] pb-[40px] text-left align-middle shadow-xl transition-all md:pl-[32px] md:pr-[72px] md:pt-[32px]">
									<div className="flex justify-end md:absolute md:top-0 md:right-0">
										<button
											type="button"
											className="flex justify-end focus:outline-none md:absolute md:top-[16px] md:right-[16px]"
											onClick={closeModal}
										>
											<ModalCloseIcon />
										</button>
									</div>
									<Dialog.Title as="div" className="flex flex-col gap-2">
										<div className="flex flex-col gap-[2px]">
											<h4 className="font-source-sans-pro text-[22px] font-semibold leading-[28px]">
												Edit User Details
											</h4>
										</div>
									</Dialog.Title>
									<EditUserDetailsForm closeModal={closeModal} />
								</Dialog.Panel>
							</div>
						</div>
					</Transition.Child>
				</Dialog>
			</Transition>
		</>
	);
}
